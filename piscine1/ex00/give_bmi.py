import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    get heights(cm) and weights(kg), calcuate BMI

    Args:
        :param height: list of height values (centimeters)
        :param weight: list of weight values (killograms)

    Returns:
        list of calculated BMI values

    Exception:
        Catches TypeError when modifying into np.array or calculating bmi
    """
    try:
        height_vector = np.array(height) * 0.01
        weight_vector = np.array(weight)
        bmi_vector = weight_vector / (height_vector * height_vector)
    except TypeError:
        print('Invalid Input')
        return None
    return bmi_vector.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Function to check bmi values if each value is over limit

    Args:
        :param bmi: list contains BMI values

    Returns:
        boolean list. True if the value is over limit

    Exception:
        never raised.
    """
    return [value > limit for value in bmi]
