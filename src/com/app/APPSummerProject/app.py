from src.util.MathUtil import MathUtility
from src.util.UserInputUtil import InputUtility
from src.com.app.APPSummerProject.Coaster import Coaster


input=InputUtility();
math=MathUtility();

#ask radius of coaster from the user
radius=input.integerValidation("Please enter the radius of the circle(Only numbers)")
coaster1=Coaster(radius);
coaster2=Coaster(radius);

# print("The area is =" +str(coaster1.getArea()));
# print("The perimeter is =" +str(coaster1.getPerimeter()));
#
# print(math.chudnovsky())
#
# print (math.findSin())

