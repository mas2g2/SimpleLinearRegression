Email : mileshshah@gmail.com | mas2g2@mail.missouri.edu
08/30/2018

Program name : Simple Linear Regression Library 1.0

 - This is a python library that was written to perform basic linear regression operations.
 - This library also includes a gradient descecnt function which is used for calculating the weight and bias for a prediction module with the smallest amount of error.
 - The functions included in this library include:
	
	1. def read_from_csv(data,filename) - This is a function which reads the contents of a csv file and returns a 2 dimensional list where all the contents of the csv file have been stored.
	2. def get_column(column_num,data) - This function returns the contents of a 2 dimensional list of floats that are found in a column of a two dimensional list
	3. def mean(array) - This function returns the mean of a list of floats.
	4. def median(array) - This function returns the median of a list of floats
	5. def mode(array) - This function returns the mode of a list
	6. def total(array) - This function returns the sum of a list of floats
	7. def squared_sum(array) - This function returns the sum of a list of floats where each item is sqsuared
	8. def variance(array) - This function returns the variance of a list of floats
	9. def sqrt(num) - This function returns the square root of a float value
	10. def standard_dev(array) - This function returns the standard deviation of a list of floats
	11. def corr_coeff(input_data,output_data) - This function returns te correlation coefficient of two lists of floats
	12. def linear_regression(input_data,output_data) - This function returns the slope and intercept of two lists of floats
	13. def prediction(new_input,slope,intercept) - This function predicts the output that will be obtained from the linear regression model
	14. def cost_function(slope,intercept,input_data,output_data) - This function calculates the half mean squared error of a prediction module
	15. def update_weight_bias(slope,intercept,learning_rate,output_data,input_data) - This function is used by the gradient descent function to obtain a weight and bias with the minimum mean squared error
	16. def gradient_desc(output_data,input_data,slope,intercept,learning_rate) - This function iterates over the weight and bias of the linear regression module and returns the slope and intercept that acheive the lowest cost
