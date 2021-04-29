class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
  def set_width(self,width):
    self.width=width
  def set_height(self,height):
    self.height=height
  def get_area(self):
    return self.width*self.height
  def get_perimeter(self):
    return (2*self.width)+(2*self.height)
  def get_diagonal(self):
    return (float(self.width**2) + (self.height**2))** .5
  def get_picture(self):
    if(self.width>50 or self.height>50):
      return "Too big for picture."
    return (int(self.width)*"*"+"\n")*int(self.height)
  def get_amount_inside(self,s):
    r=0
    if(self.width>s.width):
      if(self.height>s.height):

        n=self.width//s.width
        w=self.height//s.height
        r=max(n,w)*min(n,w)

    return r
  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)




class Square(Rectangle):
  def __init__(self,s):
    self.s=s
    super().__init__(self.s,self.s)
  def set_side(self,s):
    self.s=s
    self.width = s
    self.height = s
  def set_width(self,s):
    self.s=s
    self.width=s
    self.height=s
  def set_height(self,s):
    self.s=s
    self.width = s
    self.height = s
  def __str__(self):
    return "Square(side={})".format(self.s)


