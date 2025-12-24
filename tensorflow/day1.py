import tensorflow as tf

x = tf.constant([[1, 2, 3], [4, 5, 6]])
y = tf.constant([[7, 8, 9], [10, 11, 12]])

print(x)
print(x.shape)
print(x.dtype)
print('---'*40)
print(y)
print(y.shape)
print(y.dtype)

print('=='*20)

var1 = tf.Variable([5])
var2 = tf.Variable([6])

print(var1.shape)
print(var1.dtype)
print(var1.numpy())
print('---')

print(var1+var2)
print(var1*var2)
print(var1-var2)
print(var1/var2)
print('---')

w = tf.Variable([0.3], dtype=float)
print(w.dtype)
x = tf.Variable([-0.3])
b = tf.constant(1.0) # gives upon having datatype as int

# f = w * x
f = w * x + b # gives error upon having b's datatype as int

print(f)

a = tf.Variable([[1,2,3], [1,2,4]], dtype=tf.int32)
b = tf.Variable([[2,1,3], [4,1,3]], dtype=tf.int32)

c = a + b
print(c)