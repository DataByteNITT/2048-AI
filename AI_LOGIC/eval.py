from __future__ import print_function
import os
import neat
import visualize

from logic import *


def eval_genome(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    game_score = 0.0
    total_illegal_moves = 0
    allowed_illegal_moves = 2
    score = 0.0
    flag = None
    # Start Game
    game_matrix = init_matrix()
    i = 0
    # Run loop for NN
    while (not game_state(game_matrix)[1]) and total_illegal_moves <= allowed_illegal_moves:
        # print_game(game_matrix)
        next_move = net.activate(normalize(game_matrix))
        # x, y = map(float, input("enter x, y ").split(','))
        # next_move = (x, y)
        # print("the NN input is {}".format(normalize(game_matrix)))
        # print("the decided move is {}".format(build_move(next_move)))
        game_matrix, score, was_illegal = make_move(game_matrix, next_move)
        if was_illegal:
            total_illegal_moves += 1
        else:
            total_illegal_moves = 0
        game_score += score
        # if i == 20:
        #     print("score : {}".format(game_score))
        #     i = 0
        # i += 1

    # genome.fitness = game_score
    return game_score


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        eval_genome(genome, config)


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
    pe = neat.ParallelEvaluator(4, eval_genome)
    winner = p.run(pe.evaluate, 300)
    # winner = p.run(eval_genomes, 1)
    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))
    print('\nOutput:')

    node_names = {-1: '', -2: '', 0: 'X', 1: 'Y'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    # p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-nn')
    run(config_path)
