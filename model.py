import tensorflow as tf

# this is our Neural Network...  the players will use an instance of this class...
class Model:
    #  example... position and velocity is 2 for numstates....thats why numstates is 12
    #  num actions is num outputs...
    def __init__(self, num_states, num_actions, batch_size):
        self.num_states = num_states
        self.num_actions = num_actions
        self.batch_size = batch_size

        # Define the placeholders
        self._states = None
        self._actions = None

        # The output operations
        self._logits = None
        self._optimizer = None
        self._var_init = None

        # Setup the model
        self._define_model()

    def _define_model(self):
        self._states = tf.compat.v1.placeholder(shape=[None, self.num_states], dtype=tf.float32)
        self._q_s_a = tf.compat.v1.placeholder(shape=[None, self.num_actions], dtype=tf.float32)

        # Create dense layers
        fc1 = tf.compat.v1.layers.dense(self._states, 12, activation=tf.nn.relu)
        fc2 = tf.compat.v1.layers.dense(fc1, 18, activation=tf.nn.relu)
        fc3 = tf.compat.v1.layers.dense(fc2, 18, activation=tf.nn.relu)
        fc4 = tf.compat.v1.layers.dense(fc3, 18, activation=tf.nn.relu)
        fc5 = tf.compat.v1.layers.dense(fc4, 18, activation=tf.nn.relu)
        fc6 = tf.compat.v1.layers.dense(fc5, 18, activation=tf.nn.relu)
        fc7 = tf.compat.v1.layers.dense(fc6, 12, activation=tf.nn.relu)
        self._logits = tf.compat.v1.layers.dense(fc7, self.num_actions, activation=tf.nn.sigmoid)
        loss = tf.losses.mean_squared_error(self._q_s_a, self._logits)
        self._optimizer = tf.compat.v1.train.AdamOptimizer().minimize(loss)
        self._var_init = tf.compat.v1.global_variables_initializer()

    def predict_one(self, state, sess):
        return sess.run(self._logits, feed_dict={self._states: state.reshape(1, self.num_states)})

    def predict_batch(self, states, sess):
        return sess.run(self._logits, feed_dict={self._states: states})

    def train_batch(self, sess, x_batch, y_batch):
        sess.run(self._optimizer, feed_dict={self._states: x_batch, self._q_s_a: y_batch})


