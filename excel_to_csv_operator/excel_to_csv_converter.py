import pandas as pd, os,sys, json, glob, xlrd as xlrd


print("Inside inputConfig_File ")

if len(sys.argv)>1:
    sourceDbName, activation, lossFunction, layerNames, dbName, targetPath, operation, password, url, port, special_space_replacer, \
    targetDbName, targetPort, userName, targetHostName, inputConfigFilePath, optimizationAlgo, sourceHostName, sourceDsType, \
    modelFilePath, featureWeightPath, sourceUserName, targetUserName, targetPassword, tableName, targetDsType, sourcePassword, datasource, \
    hostName, sourcePort, sourceFilePath, paramName, query, outputResultPath, targetTableName, \
    targetDriver, includeFeatures, updater, nodeInput, edgeInput, sourceDsTypeForNode, datasourceForNode, queryForNode, sourceFilePathForNode, sourceHostNameForNode, sourceDbNameForNode, sourcePortForNode, sourceUserNameForNode, sourcePasswordForNode,targetDsDriver,targetDsUrl= (' ') * 51

    zero = lambda n: [0 for _ in range(n)]
    nEpochs, batch_size, seed, iterations, learningRate, weightInit, num_leaves, min_data,\
    numInput, numOutputs, numHidden, numLayers, numHiddenLayers, output_dim, n_estimators, colsample_bylevel, \
    min_child_weight, random_state, reg_lambda, reg_alpha, scale_pos_weight, max_delta_step, width, height, poss_outcome,\
    interval,frameGroup,possOutcome,numIter,errorScore,verbose,numJobs,numFolds,numSplits,batchSize,\
    max_features,min_df,colsample_bynode,num_classes,max_leaves,n_jobs,verbosity,subsample_freq,subsample_for_bin,min_child_samples,gpu_id = zero(46)

    none = lambda n: [None for _ in range(n)]
    otherParams, paramList,sourceDsDetails, targetDatapod, rowIdentifier, sourceAttrDetails, featureAttrDetails, sourceQuery, \
    inputSourceFileName, init, activation, optimizer, loss, average, encodingDetails, imputationDetails, modelSchema, sourceSchema, \
    inputColList, trainSetDetails, saveTrainingSet, trainSetDsType, trainSetTableName, trainSetSavePath, trainSetHostName, trainSetDbName, \
    trainSetPort, trainSetUserName, trainSetPassword, trainSetDriver, trainSetUrl, testSetDetails, testSetDsType, testSetTableName, \
    testSetSavePath, testSetHostName, testSetDbName, testSetPort, testSetUserName, testSetPassword, testSetDriver, testSetUrl, \
    boosting_type, metric, samplingTech, samplingType, objective, calcFeatureWeight, trainOverwrite, testOverwrite, resultOverwrite, \
    inputColLis, booster, mode, algoType, filters, kernel_size, padding, pool_size, dropout,kernelInitializer,strides,poolSize,\
    kernelSize,metrics,optimiser,loss,kernelInitializer,seed,base_score,colsample_bylevel,colsample_bytree,gamma,max_depth,min_child_weight,n_estimators,reg_alpha,reg_lambda \
    ,scale_pos_weight,cvType, max_depth,max_delta_step,learning_rate, execVersion,hyperParam,scoring,subsample, saveTrainVersion,scalingDetails,algoType,saveVersion, \
    saveTestVersion,grow_policy,missing,nthread,tree_method,silent,importance_type,interaction_constraints,monotone_constraints,validate_parameters,num_parallel_tree,class_weight,writeMode = none(104)


    flo = lambda n: [0.0 for _ in range(n)]
    trainPercent, testPercent, sub_feature,  base_score, colsample_bytree, subsample ,probThreshold,max_df,min_split_gain \
    = flo(9)
    output_result = dict()

    i = 0
    for eachArg in sys.argv:
        print(eachArg)
        if eachArg == "inputConfigFilePath":
            inputConfigFilePath = sys.argv[i + 1]
        i = i + 1

    #Reading of json Config file
    with open(inputConfigFilePath, 'r') as json_file:
        input_config = json.load(json_file)

    for value in input_config:
        if value == "otherParams":
            otherParams = input_config[value]

    if otherParams != None:
        for value in otherParams:
            if value == "inputFilePath":
                inputFilePath = otherParams[value]

            if value == "outputFolderPath":
                outputFolderPath = otherParams[value]

            if value == "sheetName":
                sheetName = otherParams[value]

            if value == "fileType":
                fileType = otherParams[value]


    # Printing the Variables from json config file
    print("inputFilePath: ",inputFilePath)
    print("outputFolderPath: ",outputFolderPath)
    print("sheetName: ",sheetName)
    print("fileType: ",fileType)

# iterate through all file...
def Excel_to_csv_converter(inputFilePath):
    if inputFilePath.endswith(".xlsx"):
        xls = pd.ExcelFile(inputFilePath) #accessing into sheets inside excel file
        sheets = xls.sheet_names
        for sheet in sheets:
                print("Sheet_Name: ",sheet)
                dataset = pd.read_excel(inputFilePath,sheet)
                print("dataset", dataset.head())
                #getting file name from path
                filename = inputFilePath.split(".")[0]
                print("outPut_FileName: ", sheet)
                csv_file = dataset.to_csv(f'{outputFolderPath}{sheet}.{fileType}', index=False)
                print("Saved the output csv file to: ", outputFolderPath)
        return csv_file

    else:
        for file in os.listdir(inputFilePath):
            file_name = os.path.join(inputFilePath,file)
            # Check whether file is in text format or not
            if file_name.endswith(".xlsx"):
                xls = pd.ExcelFile(file_name)  # accessing into sheets inside excel file
                sheets = xls.sheet_names
                print(sheets)
                for sheet in sheets:
                    print("input File name: ", file)
                    print("Sheet name: ",sheet)
                    dataset = pd.read_excel(file_name,sheet)
                    print("dataset", dataset.head())
                    # getting file name from path
                    filename = file.split(".")[0]
                    print("outPut_FileName: ", sheet)
                    csv_file = dataset.to_csv(f'{outputFolderPath}{filename}_{sheet}.{fileType}', index=False)
                    print("Saved the output csv file to: ", outputFolderPath)
        return csv_file



