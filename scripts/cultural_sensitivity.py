
def adjust_for_cultural_bias(data, region):
    if region == 'Asia':
        data['politeness'] *= 1.2  # Example bias adjustment
    elif region == 'Europe':
        data['directness'] *= 1.1
    return data
