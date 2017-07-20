from src.util import MathUtil
from src.util import UserInputUtil

#ask radius of coaster from the user
radius=UserInputUtil.intergerValidationOnInput("Please enter the radius of the circle(Only numbers)")

#Number of iteration for chudnovskyBig algorithm to find value of pi
no_of_iteration =UserInputUtil.intergerValidationOnInput("We are using chudnovskyBig algorithm to find the value of pi please mention "
                                                         "the no. of iteration you want us to calculate in chudnovskyBig algorithm to find"
                                                         " the value of pi (hint:More number of iteration More accurate will be the pi value "
                                                         "but increase the time to calculate it)");

#Ask user whether to round off the value of calculated pi or not
round_off_true = UserInputUtil.textValidationOnInput("Do you want us to round "
                                                     " off the value(Y/N)",["y","n","Y","N","Yes","yes","YES","NO","no"]);

#If user agrees on rounding off the value
if round_off_true=="y" or round_off_true=="Y":
    #Ask number of digit to round off
    round_off_digit = UserInputUtil.intergerValidationOnInput("Please enter the number of digit you want to consider in "
                                                              "value of pi(Max:27)");
    print(MathUtil.chudnovskyBig(no_of_iteration,1,round_off_digit))

else:
    print(MathUtil.chudnovskyBig(no_of_iteration,0,0))
