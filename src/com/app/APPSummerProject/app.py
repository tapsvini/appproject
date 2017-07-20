from src.util import MathUtil
from src.util import UserInputUtil

#Driver Program
radius=UserInputUtil.intergerValidationOnInput("Please enter the radius of the circle(Only numbers)")

no_of_iteration =UserInputUtil.intergerValidationOnInput("We are using chudnovskyBig algorithm to find the value of pi please mention "
                                                         "the no. of iteration you want us to calculate in chudnovskyBig algorithm to find"
                                                         " the value of pi (hint:More number of iteration More accurate will be the pi value "
                                                         "but increase the time to calculate it)");

round_off_true = UserInputUtil.textValidationOnInput("Do you want us to round "
                                                     " off the value(Y/N)",["y","n","Y","N","Yes","yes","YES","NO","no"]);

if round_off_true=="y" or round_off_true=="Y":
    round_off_digit = UserInputUtil.intergerValidationOnInput("Please enter the number of digit you want to consider in "
                                                              "value of pi(Max:27)");
    print(MathUtil.chudnovskyBig(no_of_iteration,1,round_off_digit))

else:
    print(MathUtil.chudnovskyBig(no_of_iteration,0,0))
