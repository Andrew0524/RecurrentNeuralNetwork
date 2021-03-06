import tensorflow as tf

# Define a decorator that is used to check if the batch size is specified.
def BatchSizeCheck(fun):
    def decofun(**kwargs):
        if kwargs.get('batch_size',None) == None :
            print('Warning, you should give a batch size. Since there''s no batch size, the loss would be large.')
        return fun(kwargs.get('output'),kwargs.get('target'),kwargs.get('batch_size',1))
    return decofun 


# This class is designed for recurrent neural network.
class RecurrentLoss():
    # the time_step parameter is designed to deal with the third type of the figure in the README.md.
    @BatchSizeCheck
    def RecurrentMeanSquared(output,target,batch_size,**kwargs):
        time_step = kwargs.get('time_step',None)
        if time_step != None :
            output = output[:,-time_step:,:]
        return tf.reduce_sum(0.5 * tf.pow(output-target,2)) / tf.constant([batch_size],dtype=tf.float64) 

