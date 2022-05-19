double average(int* salary, int salarySize){
    double totalSalary = 0;
    double max = salary[0];
    double min = salary[0];
    for (int i = 0; i < salarySize; i++){
        totalSalary += salary[i];
        if (max < salary[i]){
            max = salary[i];
        }
        if (min > salary[i]){
            min = salary[i];
        }
    }
    double average = (totalSalary - min - max)/(salarySize - 2);
    return average;
}