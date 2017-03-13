from __future__ import print_function
import os
import neat
import json
from server import send, receive

config_path = ''

async def hello(websocket, path):

    def create_game_data( action,start_game = False):
        data = {'start_game': start_game, 'action': action}
        return json.dumps(data)


    def eval_genome(genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        data = create_game_data(start_game=True, action=-1)
        send(data)
        current_game_state = receive()
        # loop to run the NN
        while(!current_game_state.over):
            next_move = net.activate(current_game_state.grid)
            send(create_game_data(action=next_move))
            current_game_state = receive()

        genome.fitness = current_game_state.score


    def eval_genomes(genomes, config):
        for genome_id, genome in genomes:
            eval_genome(genome,config)


    def run(config_file):
        # Load configuration.
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)

        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(5))

        # Run for up to 300 generations.
        winner = p.run(eval_genomes, 300)

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))

        # Show output of the most fit genome against training data.
        # print('\nOutput:')
        # winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
        # for xi, xo in zip(xor_inputs, xor_outputs):
        #     output = winner_net.activate(xi)
        #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))


        # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
        # p.run(eval_genomes, 10)
    
    run(config_path)
    
    #await websocket.send(obj) to send data
    #resp = await websocket.recv() to receive data

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-nn')
    #run(config_path)
    
    start_server = websockets.serve(hello, 'localhost', 9876)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
