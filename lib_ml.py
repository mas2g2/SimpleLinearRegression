import csv

""" Read from csv file to list """
def read_from_csv(data,filename):
    if isinstance(data,list) == False or data:
        print("ERROR : First parameter must be an empty list");
        return;
    elif filename.endswith(".csv") == False:
        print("ERROR : Second parameter must be a .csv file");
    else:
        try:
            with open(filename,"r") as csv_file:
                er = csv.reader(csv_file);
                data = list(er);
        except IOError:
            print("ERROR : File could not be opened");
        return data;


""" Get column from 2D list """
def get_column(column_num, data):
    if isinstance(column_num,int) == False:
        print("ERROR : First parameter must be an inter.");
        return;
    elif isinstance(data,list) == False and isinstance(data[0],list) == False:
        print("ERROR : Second parameter must be a 2 dimensional list");
        return;
    else:
        column = list();
        for i in range(len(data)):
            row = data[i];
            column.append(float(row[column_num]));
    return column;


""" Mean Function"""
def mean(array):
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list of floats.");
        return;
    else:
        total = 0;
        for i in array:
            if isinstance(i,float) == False:
                print("ERROR: Parameter must be a list of floats.");
                return;
            else:
                total += i;

    return total/len(array);



""" Median Function """
def median(array):
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list of floats.");
        return;
    else:
        for i in array:
            if isinstance(i,float) == False:
                print("ERROR: Parameter must be a list of floats.\n");
                return;
        array = sorted(array);
        if len(array)%2 == 0:
            median = array[int(len(array)/2)] + array[int(len(array)/2 - 1)];
            median = median/2;
            return median;
        else:
            med_index = (len(array) - 1)/2;
            median = array[int(med_index)];
            return median;


""" Mode Function """
def mode(array):
    maxcount = 0;
    mode = 0;
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list.");
        return;
    else:
        for i in array:
            count = 0;
            for j in array:
                if i == j:
                    count += 1;
            if count > maxcount:
                maxcount = count;
                mode = i;
        return mode;


""" Sum Function """
def total(array):
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list of floats.");
        return;
    else:
        total = 0;
        for i in array:
            if isinstance(i,float) == False:
                print("ERROR: Parameter must be a list of floats.");
                return;
            else:
                total += i;
        return total;



""" Squared Sum Function """
def squared_sum(array):
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list of floats.");
        return;
    else:
        total = 0;
        for i in array:
            if isinstance(i,float) == False:
               print("ERROR: Parameter must be a list of floats.");
               return;
            else:
                total += i * i;
        return total;



""" Variance Function """
def variance(array):
    if isinstance(array,list) == False:
        print("ERROR: Parameter must be a list of floats.");
        return;
    else:
        for i in array:
            if isinstance(i,float) == False:
                print("ERROR: Parameter must be a list of floats.");
                return;
        
        variance = squared_sum(array)/len(array) - mean(array)*mean(array)
        return variance;


""" Square Root Function """
def sqrt(num):
    if isinstance(num,float) == False:
        print("ERROR: Parameter must be a float value.");
        return;
    else:
        x = num;
        y = 1;
        e = 0.00001;
        while(x - y > e):
            x = (x + y)/2;
            y = num/x;
        return x;

""" Standard Deviation Function """
def standard_dev(array):
    if isinstance(array,list) == False:
        print("ERROR : Parameter must be a list of floats.");
        return;
    else:
        for i in array:
            if isinstance(i,float) == False:
                print("ERROR : Parameter must be a list of floats.");
        return sqrt(variance(array));

""" Correlation Coefficient Function """    
def corr_coeff(input_data,output_data):
    if isinstance(input_data,list) == False and isinstance(output_data,list) == False:
        print("ERROR : Parameters must be lists of floats.");
        return;
    elif len(input_data) != len(output_data):
        print("ERROR: Lists must be of the same length");
        return;
    else:
        for i in input_data:
            if isinstance(i,float) == False:
                print("ERROR : Parameters must be lists of floats.");
                return;
        for i in output_data:
            if isinstance(i,float) == False:
                print("ERROR : Parameters must be lists of floats.");
                return;
        n = len(input_data);
        sum_x = 0;
        sum_y = 0;
        sqr_sum_x = 0;
        sqr_sum_y = 0;
        sum_xy = 0;
        i = 0;
        while i < n:
            sum_x += input_data[i];
            sum_y += output_data[i];
            sum_xy += input_data[i] * output_data[i];
            sqr_sum_x += input_data[i] * input_data[i];
            sqr_sum_y += output_data[i] * output_data[i];
            i += 1;
        num = n*sum_xy - sum_x*sum_y;
        den1 = n*sqr_sum_x - sum_x*sum_x;
        den2 = n*sqr_sum_y - sum_y*sum_y;
        den = den1 * den2;
        den = sqrt(den);
        cc = num/den;
        return cc;

""" Linear Regression Function """
def linear_reggression(input_data,output_data):
    print("Slope Function");
    if isinstance(input_data,list) == False and isinstance(output_data,list) == False:
        print("ERROR : Parameters must be lists of floats.");
        return;
    elif len(input_data) != len(output_data):
        print("ERROR : Lists must be of the same length. ");
        return;
    else:
        print(" No errors "); 
        for i in input_data:
            if isinstance(i,float) == False:
                print("ERROR : Parameters must be a list of floats.");
                return;
        for i in output_data:
            if isinstance(i,float) == False:
                print("ERROR : Parameters must be a list of floats.");
                return;
        o_mean = mean(output_data);
        i_mean = mean(input_data);
        ss_xy = 0.0;
        ss_xx = 0.0;
        for i in range(len(input_data)):
            ss_xx += input_data[i]**2 - i_mean*i_mean*len(input_data);
            ss_xy += input_data[i] * output_data[i] - i_mean*o_mean*len(input_data);
        slope = ss_xy/ss_xx;
        intercept = o_mean - slope*i_mean;
        return slope,intercept;



""" Prediction Function """
def prediction(new_input,slope,intercept):
    if isinstance(new_input,float) == False and isinstance(slope,float) == False and isinstance(intercept,float) == False:
        print("ERROR : All parameters must be float values.");
        return;
    else:
        return slope*new_input + intercept;


""" Cost or Half Mean Squared Error Function """
def cost_function(slope,intercept,input_data,output_data):
    if isinstance(slope,float) == False and isinstance(intercept,float) == False:
        print("ERROR : Slope must be a float value and/or Intercept must be a float value.");
        return;
    elif len(input_data) != len(output_data):
        print("ERROR : Lists must be of the same length.");
        return;
    else:
        error = list();
        for i in range(len(input_data)):
            if isinstance(input_data[i],float) == False and isinstance(output_data,float) == False:
                print("ERROR : Parameters must be a list of floats.");
                return;
            else:
                error.append(float(output_data[i] - linear_prediction(input_data[i],slope,intercept)));

        cost = squared_sum(error)/float((2*len(input_data)));
        return cost;


""" Update Weight (Slope) and Bias (Intercept) Function """
def update_weight_bias(slope,intercept,learning_rate,output_data,input_data):
    if isinstance(slope,float) == False and isinstance(intercept,float) == False and isinstance(learning_rate,float) == False:
        print("ERROR : Slope, intercept and learning rate (first three parameters of function) must be float values.");
        return;
    elif isinstance(output_data,list) == False and isinstance(input_data,float) == False:
        print("ERROR : Last two parameters must be lists of floats.");
        return;
    elif len(output_data) != len(input_data):
        print("ERROR : Lists must be of the same length.");
        return;
    else:
        slope_der = list();
        intercept_der = list();
        for i in range(len(output_data)):
            if isinstance(input_data[i],float) == False and isinstance(output_data,float) == False:
                print("ERROR : Last two parameters must be lists of floats.");
                return;
            else:
                slope_der.append(float(-2*input_data[i]*(output_data[i] - linear_prediction(input_data[i],slope,intercept))));
                intercept_der.append(float(-2*(output_data[i] - linear_prediction(input_data[i],slope,intercept))));
        intercept -= learning_rate*total(intercept_der)/float(len(input_data));
        slope -= learning_rate*total(slope_der)/float(len(input_data));
        return slope,intercept;



""" Gradient Descent Function """
def grad_desc(output_data,input_data,slope,intercept,learning_rate):
    if isinstance(output_data,list) == False and isinstance(input_data,list) == False:
        print(" ERROR : First two parameters must be lists of floats, first one must be the output data and the second one must be the input data. ");
        return;
    elif isinstance(slope,float) == False and isinstance(intercept,float) == False and isinstance(learning_rate,float) == False:
        print(" ERROR : Last three parameters must be float values. ");
        return;
    elif len(output_data) != len(input_data):
        print("ERROR : Lists must be of the same length. ");
        return;
    else:
        error = cost_function(slope,intercept,input_data,output_data);
        prev_error = error;
        while prev_error > error :
            print("Weight of prediction model : ",slope," Bias of prediction model : ",intercept," Cost of prediction model : ",error);
            slope,intercept = update_weight_bias(slope,intercept,learning_rate,output_data,input_data);
            prev_error = error;
            error = cost_function(slope,intercept,input_data,output_data);
        return slope,intercept;
