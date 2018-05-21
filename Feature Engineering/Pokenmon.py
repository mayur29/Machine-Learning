from pyspark import SparkContext


sc = SparkContext.getOrCreate()

data = ['Hello' , 'I' , 'AM', 'Ankit ', 'Gupta']
Rdd = sc.parallelize(data)
Rdd1 = Rdd.map(lambda x: (x,1))
Rdd1.collect()