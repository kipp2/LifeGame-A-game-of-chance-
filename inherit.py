class Parentclass:
	def feature1(self):
		print("feature1 from prentclass is running...")
		
class Childclass1:
    def feature2(self):
        print("feature2 from childclass1 is running...")
		
class Childclass2(Parentclass,Childclass1):
	def feature3(self):
		print("feature3 from childclass2 is running..")

obj = Childclass2()
obj.feature1()
obj.feature2()
obj.feature3()

