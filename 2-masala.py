class TupleSort:
    @staticmethod
    def sort_tuple(tuple1, tuple2):
        assert isinstance(tuple1, tuple) and isinstance(tuple2, tuple), "Inputs should be tuples"

        common_elements = list(set(tuple1) & set(tuple2))

        return common_elements



tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

result = TupleSort.sort_tuple(tuple1, tuple2)
print(result)
