# **bobify-goals**

This Python script automates the process of converting a simple list of goals and key results from a CSV file into a structured Excel file, which is compatible for bulk import HiBob

The script handles the grouping of multiple key results under a single goal, populates key fields with default values, and outputs a correctly formatted .xlsx file.

### **Prerequisites**

To use this script, you must have Python installed on your computer. You also need to install the required dependencies.

### **Installation**

1. **Install the required libraries** using the requirements.txt file. Navigate to the project directory in your terminal and run:  
   ```
   pip install \-r requirements.txt
   ```

### **Setup**

1. Create your input data file:  
   Create a file named goals\_input.csv in the same directory as the script.
   Or use the one provided.
3. Format the CSV file with the correct header:  
   The input CSV file must have the following header row exactly as shown:  
   ```
   Email,GoalName,KeyResult,Timeframe
   ...
   ```

4. **Populate the goals\_input.csv file** with your data. Each line should contain an email address, a goal name, a key result, and the time frame for the goal.  
 Timeframe accepts the following values: Previous quarter, This quarter, This half, Next quarter, Previous year, This year, Next year, Date(MM/DD/YY)
 
   
   **Example goals\_input.csv content:**  
   ```
   Email,GoalName,KeyResult,Timeframe  
   user1@example.com,ORM L2,"Complex querying capabilities in ORM (e.g., subqueries, grouping)",This quarter  
   user1@example.com,ORM L2,"Transactions, including commit and rollback operations.",This quarter  
   user2@example.com,Software Design,Design Patterns \- Creational Patterns,This quarter  
   user2@example.com,Software Design,Design Patterns \- Structural Patterns,This quarter
   ```

### **How to Run**

```
python bobify.py
```

### **Output**

The script will generate a new Excel file named **goals\_import\_v3\bob.xlsx** in the same directory. This file will be formatted correctly with all the necessary columns, including Status set to **'On Track'**, Visibility set to **'Personal'**, and all Measure key result by fields set to **'Percentage'**.
This excel file can be imported and validated in bob imports page
