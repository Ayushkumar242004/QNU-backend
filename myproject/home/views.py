from django.http import JsonResponse
from tests.frequency_test import FrequencyTest  # Adjust the import path accordingly
from tests.runs_test import RunTest  # Adjust the import path accordingly
from tests.approximate_entropy_test import ApproximateEntropy
from tests.linear_complexity_test import ComplexityTest
from tests.template_matching_test import TemplateMatching
from tests.universal_test import Universal
from tests.serial_test import Serial
from tests.cumulative_sums_test import CumulativeSums
from tests. random_excursions_test import RandomExcursions
from tests.Matrix import Matrix
from tests.spectral import SpectralTest
from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest
from PIL import Image as PILImage
from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest


from tests.Birthday_spacings_test import BirthdaySpacingsTest


def run_frequency_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the monobit_test method from the FrequencyTest class
    p_value, result = FrequencyTest.monobit_test(binary_data)

    print("FrequencyTest p_value:", p_value)
    print("FrequencyTest Result:", result)
    
    # Prepare the response data
    if result == 1:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)
def run_frequency_block_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)


    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Call the block_frequency method
    p_value, result = FrequencyTest.block_frequency(binary_data)

    print("run_frequency_block_test p_value:", p_value)
    print("run_frequency_block_test Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)





def run_birthday_spacings_test(request):
    # Example binary data received from the request query parameters
    binary_data_str = request.GET.get('binary_data', '')

    # Print the request URL and parameters for debugging
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Convert binary string to a list of integers
    if binary_data_str:
        # Ensure only '0' and '1' are considered
        binary_data = [int(bit) for bit in binary_data_str if bit in '01']
    else:
        return JsonResponse({'error': 'Invalid or missing binary data.'}, status=400)

    # Check if the converted data has at least two points
    if len(binary_data) < 2:
        return JsonResponse({'error': 'Insufficient data. At least two data points are required.'}, status=400)

    # Call the Birthday Spacings Test method
    p_value, result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)

    print("run_birthday_spacings_test p_value:", p_value)
    print("run_birthday_spacings_test Result:", result)

    # Prepare the response data
    result_text = "random number" if result else "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


