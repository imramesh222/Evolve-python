class  A:
  # protected
  _x=10
  # private
  __y=20
  # public
  xy=20
  def __init__(self):
    print(f"Protected value ={self._x} ")
    print(f"Private value ={self.__y} ")
class B(A):
    def __init__(self):
        # print(f"Protected value ={self._x} ")
        print(f"Private value ={self.__y} ")
obj=A()
obj=B()