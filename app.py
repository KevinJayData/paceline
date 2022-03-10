import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import graphs


def main(graph=True):
    data = pd.read_csv('data-take-home-data.csv')

    data['did_not_claim'] = np.where((data['hit_streak'] == 1) & (data['claimed_reward'] == 0), 1, 0)


    graphs.claimed_reward_graph(data, graph)
    graphs.days_exercised_graph(data, graph)
    graphs.exercise_mins_graph(data, graph)
    graphs.install_source_variant_graph(data, graph)
    graphs.did_not_claim_graph(data, graph)
    graphs.did_not_claim_by_device_graph(data, graph)
    graphs.install_source_did_not_claim_graph(data, graph)

    experiment_analysis(data)



def experiment_analysis(data):
    """
    Confirming the experiment populations will not introduce bias
    :param data: pandas df
    :return: Nothing, this func contains my notes
    """
    # Ensure populations are consistent across experiments
    # age looks good
    data.groupby('variant')['age'].mean()
    data.groupby('variant')['age'].std()

    # device_linked, looks like 2k each exactly. Increased rewards has twice the number of Garmin, slightly less Apple
    data.groupby('variant')['device_linked'].count()
    data.groupby('variant')['device_linked'].value_counts()

    # exercise_minutes, Control has higher mean, however well within 95% CI so not a statistically significant concern
    data.groupby('variant')['exercise_mins'].mean()
    data.groupby('variant')['exercise_mins'].std()

    # Exactly 1k observations per week
    data.week.value_counts()

    # look quickly at claim rate
    data.groupby(['variant', 'week'])['claimed_reward'].mean()
    data.groupby(['variant', 'week'])['claimed_reward'].std()

    # "The number of users in a given week that claim rewards is much lower than the number of users
    # who hit their Streak for the week"

    # Think about a "funnel" how many people from each group hit and then claim?
    streak = data.groupby('variant')['hit_streak'].value_counts()
    reward = data.groupby('variant')['claimed_reward'].value_counts()
    print(reward['Control'][1]/streak['Control'][1]) # 20.3% of control claimed their rewards
    print(reward['Increased Rewards'][1] / streak['Increased Rewards'][1]) # 20.4% of increased claimed

    # Out of 1k users, over half are not claiming any rewards and only 16 claimed all 4 weeks
    data.groupby(['userid'])['claimed_reward'].sum().value_counts()
    data[data.variant == 'Control'].groupby(['variant', 'userid'])['claimed_reward'].sum().value_counts() # Control
    data[data.variant == 'Increased Rewards'].groupby(['variant', 'userid'])['claimed_reward'].sum().value_counts() # Increased Rewards

    # Lets look now at the did_not_claim population.  we want to reduce this population as much as possible.
    data.groupby('variant')['did_not_claim'].value_counts()
    data.groupby(['userid'])['did_not_claim'].sum().value_counts()
    data[data.variant == 'Control'].groupby(['variant', 'userid'])['did_not_claim'].sum().value_counts().sort_index()
    data[data.variant == 'Increased Rewards'].groupby(['variant', 'userid'])['did_not_claim'].sum().value_counts().sort_index()


    # did_not_claim/hit_steak
    by_user = data.groupby(['userid']).sum()
    by_user['did_not_claim_rate'] = by_user.did_not_claim/by_user.hit_streak
    variant_data = data.groupby(['userid'])['variant'].value_counts()
    variant_data = pd.DataFrame(list(variant_data.index), columns=['userid', 'variant'])
    combined_data = by_user.merge(variant_data, on='userid')
    combined_data.groupby(['variant'])['did_not_claim_rate'].value_counts().sort_values(ascending=False)




if __name__ == "__main__":
    main()