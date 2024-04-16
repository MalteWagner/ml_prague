from models import Baseline_cbr_mb
from train import get_min_max_dict
from predict import predict
import tensorflow as tf


if __name__ == "__main__":

    model = Baseline_cbr_mb()
 

    # Compute normalization values
    model.set_min_max_scores(
        get_min_max_dict(
            tf.data.Dataset.load("data\\gnnet-ch23-dataset-cbr-mb_prepro", compression="GZIP"),
            model.min_max_scores_fields,
        )
    )
    # Compile the model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.MeanAbsolutePercentageError(),
    )
    
    # Load weights of latest checkpoint
    # Checkpoint names are the latest index files in the ckpt folder. IMPORTANT: Remove .index at end of file name.
    model.load_weights("ckpt\\Baseline_cbr_mb_full_data\\55-42.9441")

    # Load the test dataset
    ds = tf.data.Dataset.load("data\\part_test_prepped", compression="GZIP")

    # Predict
    predict(ds, model, "predictions", "verification_files\\submission_verification.txt")