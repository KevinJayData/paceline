import matplotlib.pyplot as plt
import seaborn as sns


def save_close(file_name):
    """
    Used to reduce code duplication, saves graph in dir, closes and clears the plot
    :param file_name: string of the desired filename, must include extension, usually .png
    :return: Nothing.
    """
    plt.savefig('graphs_dir/'+file_name)
    plt.close()
    plt.cla()
    plt.clf()


def claimed_reward_graph(data, graph):
    """
    Creates graph to look at mean claimed_reward rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'device_linked'])['claimed_reward'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'device_linked'], values='claimed_reward')

    if graph:
        sns.set_theme()
        plt.figure(figsize=(9, 6))
        for variant, device in graph_pivot:
            color_dict = {'Applewatch': 'red', 'Garmin': 'blue', 'FitBit':'green'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][device], label=device+' - '+variant, linestyle=linestyle, color=color_dict[device])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('claimed_reward %')
        plt.title('Percent of Users claiming Rewards by device_linked type')
        save_close('claimed_reward_graph')


def exercise_mins_graph(data, graph):
    """
    Creates graph to look at mean minutes exercised across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'device_linked'])['exercise_mins'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'device_linked'], values='exercise_mins')

    if graph:
        sns.set_theme()
        plt.figure(figsize=(9, 6))
        for variant, device in graph_pivot:
            color_dict = {'Applewatch': 'red', 'Garmin': 'blue', 'FitBit':'green'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][device], label=device+' - '+variant, linestyle=linestyle, color=color_dict[device])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('Minutes')
        plt.title('Mean Minutes of Exercise per user per week')
        save_close('exercise_mins_graph')


def days_exercised_graph(data, graph):
    """
    Creates graph to look at mean claimed_reward rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'device_linked'])['days_exercised'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'device_linked'], values='days_exercised')

    if graph:
        sns.set_theme()
        plt.figure(figsize=(9, 6))
        for variant, device in graph_pivot:
            color_dict = {'Applewatch': 'red', 'Garmin': 'blue', 'FitBit':'green'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][device], label=device+' - '+variant, linestyle=linestyle, color=color_dict[device])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('Days')
        plt.title('Mean days_exercised per user per week')
        save_close('days_exercised_graph')


def install_source_variant_graph(data, graph):
    """
    Creates graph to look at mean claimed_reward rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'install_source'])['claimed_reward'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'install_source'], values='claimed_reward')

    if graph:
        plt.figure(figsize=(9, 6))
        sns.set_theme()
        for variant, install_source in graph_pivot:
            color_dict = {'organic': 'yellow', 'paid_ad': 'purple', 'referred':'orange'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][install_source], label=install_source+' - '+variant, linestyle=linestyle, color=color_dict[install_source])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('claimed_reward %')
        plt.title('Claimed Reward % per week by Install Source')
        save_close('install_source_variant_graph')


def did_not_claim_graph(data, graph):
    """
    Creates graph to look at did_not_claim rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant'])['did_not_claim'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant'], values='did_not_claim')

    if graph:
        plt.figure(figsize=(9, 6))
        sns.set_theme()
        for variant in graph_pivot:
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant], label=variant, linestyle=linestyle)
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('did_not_claim %')
        plt.title('did_not_claim rate by Variant Population per week')
        save_close('did_not_claim_graph')


def did_not_claim_by_device_graph(data, graph):
    """
    Creates graph to look at did_not_claim rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'device_linked'])['did_not_claim'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'device_linked'], values='did_not_claim')

    if graph:
        plt.figure(figsize=(9, 6))
        sns.set_theme()
        for variant, device in graph_pivot:
            color_dict = {'Applewatch': 'red', 'Garmin': 'blue', 'FitBit':'green'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][device], label=device+' - '+variant, linestyle=linestyle, color=color_dict[device])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('did_not_claim %')
        plt.title('did_not_claim rate by Device Type per week')
        save_close('did_not_claim_by_device_graph')


def install_source_did_not_claim_graph(data, graph):
    """
    Creates graph to look at did not claim rate across device types and experiment variants.
    :param data: pandas df of the csv
    :param graph: Boolean, I set to False when I want to avoid graphing for speed reasons
    :return: Functionally nothing, however this outputs a graph to the graphs_dir/ folder
    """
    graph_data = data.groupby(['week', 'variant', 'install_source'])['did_not_claim'].mean().reset_index()
    graph_pivot = graph_data.pivot(index='week', columns=['variant', 'install_source'], values='did_not_claim')

    if graph:
        plt.figure(figsize=(9, 6))
        sns.set_theme()
        for variant, install_source in graph_pivot:
            color_dict = {'organic': 'yellow', 'paid_ad': 'purple', 'referred':'orange'}
            linestyle = '--' if variant == 'Control' else '-' # Control gets dashed lines for clarity
            plt.plot(graph_pivot.index, graph_pivot[variant][install_source], label=install_source+' - '+variant, linestyle=linestyle, color=color_dict[install_source])
        plt.legend()
        plt.xlabel('Week')
        plt.ylabel('did_not_claim %')
        plt.title('Did Not Claim % per week by Install Source')
        save_close('install_source_did_not_claim_graph')