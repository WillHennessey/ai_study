import numpy as np
import time


def vector_creation_example():
    # NumPy routine which allocate memory and fill arrays with value
    a = np.zeros(4)
    print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
    a = np.zeros((4,))
    print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
    a = np.random.random_sample(4)
    print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

    # NumPy routine which allocate memory and fill arrays with value but do not accept shape as input argument
    a = np.arange(4.)
    print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
    a = np.random.rand(4)
    print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

    # NumPy routine which allocate memory and fill with user specified values
    a = np.array([5, 4, 3, 2])
    print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
    a = np.array([5., 4, 3, 2])
    print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")


def operations_on_vectors():
    # vector indexing operations on 1-D vectors
    a = np.arange(10)
    print(a)

    # access an element
    print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")

    # access the last element, negative indexes count from the end
    print(f"a[-1] = {a[-1]}")

    # indexes must be within the range of the vector, or they will produce and error
    try:
        a[10]
    except Exception as e:
        print("The error message you'll see is:")
        print(e)


def slicing_examples():
    # vector slicing operations
    a = np.arange(10)
    print(f"a         = {a}")

    # access 5 consecutive elements (start:stop:step)
    c = a[2:7:1]
    print("a[2:7:1] = ", c)

    # access 3 elements separated by two
    c = a[2:7:2]
    print("a[2:7:2] = ", c)

    # access all elements index 3 and above
    c = a[3:]
    print("a[3:]    = ", c)

    # access all elements below index 3
    c = a[:3]
    print("a[:3]    = ", c)

    # access all elements
    c = a[:]
    print("a[:]     = ", c)


def single_vector_operations():
    a = np.array([1, 2, 3, 4])
    print(f"a             : {a}")
    # negate elements of a
    b = -a
    print(f"b = -a        : {b}")

    # sum all elements of a, returns a scalar
    b = np.sum(a)
    print(f"b = np.sum(a) : {b}")

    b = np.mean(a)
    print(f"b = np.mean(a): {b}")

    b = a ** 2
    print(f"b = a**2      : {b}")


def vector_element_operations():
    a = np.array([1, 2, 3, 4])
    b = np.array([-1, -2, 3, 4])
    print(f"Binary operators work element wise: {a + b}")

    # try a mismatched vector operation
    c = np.array([1, 2])
    try:
        a + c
    except Exception as e:
        print("The error message you'll see is:")
        print(e)


def scalar_vector_operations():
    a = np.array([1, 2, 3, 4])

    # multiply a by a scalar
    b = 5 * a
    print(f"b = 5 * a : {b}")


def my_dot(a, b):
    """
      Compute the dot product of two vectors

       Args:
         a (ndarray (n,)):  input vector
         b (ndarray (n,)):  input vector with same dimension as a

       Returns:
         x (scalar):
       """
    x = 0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x


def my_dot_example():
    # test 1-D
    a = np.array([1, 2, 3, 4])
    b = np.array([-1, 4, 3, 2])
    print(f"my_dot(a, b) = {my_dot(a, b)}")

    # test 1-D
    a = np.array([1, 2, 3, 4])
    b = np.array([-1, 4, 3, 2])
    c = np.dot(a, b)
    print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape} ")
    c = np.dot(b, a)
    print(f"NumPy 1-D np.dot(b, a) = {c}, np.dot(a, b).shape = {c.shape} ")


def vector_vs_loop_example():
    np.random.seed(1)
    a = np.random.rand(10000000)  # very large arrays
    b = np.random.rand(10000000)

    tic = time.time()  # capture start time
    c = np.dot(a, b)
    toc = time.time()  # capture end time

    print(f"np.dot(a, b) =  {c:.4f}")
    print(f"Vectorized version duration: {1000 * (toc - tic):.4f} ms ")

    tic = time.time()  # capture start time
    c = my_dot(a, b)
    toc = time.time()  # capture end time

    print(f"my_dot(a, b) =  {c:.4f}")
    print(f"loop version duration: {1000 * (toc - tic):.4f} ms ")
    # remove these big arrays from memory
    del a
    del b


def vector_vector_example():
    # show common Course 1 example
    x = np.array([[1], [2], [3], [4]])
    w = np.array([2])
    c = np.dot(x[1], w)

    print(f"X[1] has shape {x[1].shape}")
    print(f"w has shape {w.shape}")
    print(f"c has shape {c.shape}")


def matrix_creation_example():
    a = np.zeros((1, 5))
    print(f"a shape = {a.shape}, a = {a}")

    a = np.zeros((2, 1))
    print(f"a shape = {a.shape}, a = {a}")

    a = np.random.random_sample((1, 1))
    print(f"a shape = {a.shape}, a = {a}")

    # NumPy routine which allocate memory and fill with user specified values
    a = np.array([[5], [4], [3]])
    print(f" a shape = {a.shape}, np.array: a = {a}")
    a = np.array([[5],  # One can also
                  [4],  # separate values
                  [3]])  # into separate rows
    print(f" a shape = {a.shape}, np.array: a = {a}")


def indexing_matrices_example():
    # vector indexing operations on matrices
    a = np.arange(6).reshape(-1, 2)  # reshape is a convenient way to create matrices
    print(f"a.shape: {a.shape}, \na= {a}")

    # access an element
    print(
        f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]}, "
        f"type(a[2,0]) = {type(a[2, 0])} Accessing an element returns a scalar\n")

    # access a row
    print(f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")


def slicing_matrices_example():
    # vector 2-D slicing operations
    a = np.arange(20).reshape(-1, 10)
    print(f"a = \n{a}")

    # access 5 consecutive elements (start:stop:step)
    print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

    # access 5 consecutive elements (start:stop:step) in two rows
    print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

    # access all elements
    print("a[:,:] = \n", a[:, :], ",  a[:,:].shape =", a[:, :].shape)

    # access all elements in one row (very common usage)
    print("a[1,:] = ", a[1, :], ",  a[1,:].shape =", a[1, :].shape, "a 1-D array")
    # same as
    print("a[1]   = ", a[1], ",  a[1].shape   =", a[1].shape, "a 1-D array")


if __name__ == '__main__':
    vector_creation_example()
    operations_on_vectors()
    slicing_examples()
    single_vector_operations()
    vector_element_operations()
    scalar_vector_operations()
    my_dot_example()
    vector_vs_loop_example()
    vector_vector_example()
    matrix_creation_example()
    indexing_matrices_example()
    slicing_matrices_example()
