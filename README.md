# python-mock-demo
python mock demo for unit test


mocking is a little bit tricky, especially when we want to mock a iterable.

When we want to access the iterable through index, like m[1], m[1000] ...
We can do it like:
    m = MagicMock()
    m.__getitem__.return_value = 2
    self.assertEqual(m[0], 2)     #the first time we get item
    self.assertEqual(m[1000], 2)  #we always get the same value

When we want to access the iterable in for loop,
We can do it like:
    m.__iter__.return_value = iter([1, 2])
    result = [x for x in m]
    print('result:', result)  #[1, 2]

When we want to check whether or not an item exists in iterable,
We can do it like:
    m.__contains__.return_value = True
    self.assertEqual(3 in m, True)
    self.assertEqual('anything' in m, True)  #anything in m will return True

