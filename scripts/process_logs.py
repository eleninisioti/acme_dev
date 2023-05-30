import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":

    results_dir = "server_results/acme/20230526-154853/logs"

    with open(results_dir + "/actor/logs.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        actor_data = [row for row in reader]


    with open(results_dir + "/evaluator/logs.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        evaluator_data = [row for row in reader]


    with open(results_dir + "/learner/logs.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        learner_data = [row for row in reader]

    print(learner_data[-1])
    actor_steps = [int(row[1]) for row in evaluator_data[1:]]
    episode_return = [float(row[6]) for row in evaluator_data[1:]]
    plt.plot(actor_steps, episode_return)
    print("yo")



