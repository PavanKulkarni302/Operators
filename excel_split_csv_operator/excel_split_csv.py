import pandas as pd,sys,json

if len(sys.argv)>1 and sys.argv[1] !='excel_csv_converter':
    inputConfigFilePath, = (' ') * 1

    i = 0
    for eachArg in sys.argv:

        if eachArg == "inputConfigFilePath":
            inputConfigFilePath = sys.argv[i + 1]
        i = i + 1

    #Reading json file and importing all necessary parameters...
    with open(inputConfigFilePath, 'r') as json_file:
        input_config = json.load(json_file)

    for item in input_config:
        if item == 'otherParams':
            otherParams = input_config[item]

    if otherParams != None:
        for value in otherParams:
            if value == "inputFilePath":
                Input_Filepath = otherParams[value]

            if value == "outputFolderPath":
                output_Filepath = otherParams[value]

            if value == "splitFiles":
                split_Files = int(otherParams[value])

            if value == "splitRecords":
                split_Records = int(otherParams[value])

            if value == "fileType":
                file_Type = otherParams[value]

    # Printing all the parameters...
    print("inputFilepath:", Input_Filepath)
    print("outputFolderPath:", output_Filepath)
    print("splitFiles:", split_Files)
    print("splitRecords:", split_Records)
    print("fileType:", file_Type)

    #Read the input excel file...
    data = pd.read_excel(Input_Filepath)

    #defined the splitting constraints
    size = split_Records
    k = round(len(data)/size)

    #Splitting the data and stroring as a csv file...
    for i in range(k):
        df = data[size * i:size * (i + 1)]
        df.to_csv(f'{output_Filepath}output_xls_{i + 1}.{file_Type}', index=False)
    print("Output_files are saved to: ",output_Filepath)



