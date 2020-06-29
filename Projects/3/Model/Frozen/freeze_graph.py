import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2


print(tf.__version__)  # 2.0.

with open("Model/model.json") as file:
    m_json = file.read()

model = tf.keras.models.model_from_json(m_json)
model.load_weights("Model/model.h5")

model.summary()
print("")


def freeze(model, outputdir='./'):

    # Convert Keras model to ConcreteFunction
    full_model = tf.function(lambda x: model(x))
    full_model = full_model.get_concrete_function(
        tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype)
    )

    frozen_func = convert_variables_to_constants_v2(full_model)
    frozen_func.graph.as_graph_def()
    # Save frozen graph from frozen ConcreteFunction to hard drive
    tf.io.write_graph(graph_or_graph_def=frozen_func.graph,
                      logdir=outputdir,
                      name="frozen_graph.pb",
                      as_text=False)

    layers = [op.name for op in frozen_func.graph.get_operations()]

    print("Frozen model layers: ")
    for layerName in layers:
        print(f"layer: {layerName}")

    print("-" * 50)
    print("Frozen model inputs: ")
    print(frozen_func.inputs)
    print("Frozen model outputs: ")
    print(frozen_func.outputs)


# Run the TF2.0 freezer
freeze(model, 'Model/Frozen')
