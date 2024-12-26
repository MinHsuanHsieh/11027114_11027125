# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType

data_sample = PandasParameterType(pd.DataFrame({"function_pair": pd.Series(["example_value"], dtype="object"), "danceability_mean": pd.Series([0.0], dtype="float32"), "danceability_stdev": pd.Series([0.0], dtype="float32"), "energy_mean": pd.Series([0.0], dtype="float32"), "energy_stdev": pd.Series([0.0], dtype="float32"), "loudness_mean": pd.Series([0.0], dtype="float32"), "loudness_stdev": pd.Series([0.0], dtype="float32"), "mode_mean": pd.Series([0.0], dtype="float32"), "mode_stdev": pd.Series([0.0], dtype="float32"), "speechiness_mean": pd.Series([0.0], dtype="float32"), "speechiness_stdev": pd.Series([0.0], dtype="float32"), "acousticness_mean": pd.Series([0.0], dtype="float32"), "acousticness_stdev": pd.Series([0.0], dtype="float32"), "liveness_mean": pd.Series([0.0], dtype="float32"), "liveness_stdev": pd.Series([0.0], dtype="float32"), "valence_mean": pd.Series([0.0], dtype="float32"), "valence_stdev": pd.Series([0.0], dtype="float32"), "tempo_mean": pd.Series([0.0], dtype="float32"), "tempo_stdev": pd.Series([0.0], dtype="float32"), "instrumentalness_mean": pd.Series([0.0], dtype="float32"), "instrumentalness_stdev": pd.Series([0.0], dtype="float32"), "0_count": pd.Series([0], dtype="int8"), "1_count": pd.Series([0], dtype="int8"), "2_count": pd.Series([0], dtype="int8"), "3_count": pd.Series([0], dtype="int8"), "4_count": pd.Series([0], dtype="int8"), "5_count": pd.Series([0], dtype="int8"), "6_count": pd.Series([0], dtype="int8"), "7_count": pd.Series([0], dtype="int8"), "8_count": pd.Series([0], dtype="int8"), "9_count": pd.Series([0], dtype="int8"), "10_count": pd.Series([0], dtype="int8"), "11_count": pd.Series([0], dtype="int8")}))
input_sample = StandardPythonParameterType({'data': data_sample})
method_sample = StandardPythonParameterType("predict")
sample_global_params = StandardPythonParameterType({"method": method_sample})

result_sample = NumpyParameterType(np.array(["example_value"]))
output_sample = StandardPythonParameterType({'Results':result_sample})

try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script_v2')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = "model.pkl"
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    #log_server.update_custom_dimensions({'model_name': path_split[-3], 'model_version': path_split[-2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise

@input_schema('GlobalParameters', sample_global_params, convert_to_provided_type=False)
@input_schema('Inputs', input_sample)
@output_schema(output_sample)
def run(Inputs, GlobalParameters={"method": "predict"}):
    data = Inputs['data']
    if GlobalParameters.get("method", None) == "predict_proba":
        result = model.predict_proba(data)
    elif GlobalParameters.get("method", None) == "predict":
        result = model.predict(data)
    else:
        raise Exception(f"Invalid predict method argument received. GlobalParameters: {GlobalParameters}")
    if isinstance(result, pd.DataFrame):
        result = result.values
    return {'Results':result.tolist()}


if __name__ == "__main__":
    init()
    test_sample = {
        'Inputs': {
            'data': pd.DataFrame({
                'function_pair': ['example_value'],
                'danceability_mean': [0.0],
                'danceability_stdev': [0.0],
                'energy_mean': [0.0],
                'energy_stdev': [0.0],
                'loudness_mean': [0.0],
                'loudness_stdev': [0.0],
                'mode_mean': [0.0],
                'mode_stdev': [0.0],
                'speechiness_mean': [0.0],
                'speechiness_stdev': [0.0],
                'acousticness_mean': [0.0],
                'acousticness_stdev': [0.0],
                'liveness_mean': [0.0],
                'liveness_stdev': [0.0],
                'valence_mean': [0.0],
                'valence_stdev': [0.0],
                'tempo_mean': [0.0],
                'tempo_stdev': [0.0],
                'instrumentalness_mean': [0.0],
                'instrumentalness_stdev': [0.0],
                '0_count': [0],
                '1_count': [0],
                '2_count': [0],
                '3_count': [0],
                '4_count': [0],
                '5_count': [0],
                '6_count': [0],
                '7_count': [0],
                '8_count': [0],
                '9_count': [0],
                '10_count': [0],
                '11_count': [0]
            })
        },
        'GlobalParameters': {"method": "predict"}
    }
    
    prediction = run(test_sample['Inputs'], test_sample['GlobalParameters'])
    print(prediction)
