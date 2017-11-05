setwd("C:\\Users\\David Ouyang\\Dropbox\\StatisticalAnalysis\\Sinonasal\\Final Data Set")
library(ggplot2)

data <- read.csv("subsetNeurosurgery.csv")
summary(data)
str(data)

data <- read.csv("surgicalCasesWComplications.csv")
summary(data)
str(data)

summary(data[data$volume == "high" & data$los > 0,])
summary(data[data$volume != "high"& data$los > 0,])

sd(data[data$volume == "high" & data$los > 0,]$los)
sd(data[data$volume != "high" & data$los > 0,]$los)

summary(data[data$los > 0,]$los)
sd(data[data$los > 0,]$los)

data <- read.csv("HospitalAvgPerYear.csv")
str(data)

summary(data[data$Category == "high",])
summary(data[data$Category != "high",])

3/30
5/30
22/30

27/30
3/30

29/30
1/30

79/1061
106/1061
128/1061

113/828
254/828
461/828

346/828
482/828

707/828
121/828

165/2789 
130/2789 
169/2789 

data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)

diags <- c(as.character(data$d1), data$d2, data$d3, data$d4, data$d5, data$d6) 
diags <- c(diags, data$d7, data$d8, data$d9, data$d10, data$d11) 
diags <- c(diags, data$d12, data$d13, data$d14, data$d15 )

write.csv(table(diags), "NormalizedDiags.csv")


data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)
data <- data[data$volume == "high",]

diags <- c(as.character(data$d1), data$d2, data$d3, data$d4, data$d5, data$d6) 
diags <- c(diags, data$d7, data$d8, data$d9, data$d10, data$d11) 
diags <- c(diags, data$d12, data$d13, data$d14, data$d15 )

write.csv(table(diags), "HighVolumeNormalizedDiags.csv")

data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)
data <- data[data$volume != "high",]

diags <- c(as.character(data$d1), data$d2, data$d3, data$d4, data$d5, data$d6) 
diags <- c(diags, data$d7, data$d8, data$d9, data$d10, data$d11) 
diags <- c(diags, data$d12, data$d13, data$d14, data$d15 )

write.csv(table(diags), "LowVolumeNormalizedDiags.csv")

87/3850
71/3850
30/3850
17/3850
16/3850
8/3850
71/3850
239/3850
51/3850
76/3850
46/3850
312/3850

4/1061
14/1061
16/1061
9/1061
3/1061
8/1061
1/1061
127/1061
87/1061
13/1061
20/1061
12/1061
110/1061

26/2789
57/2789
55/2789
21/2789
14/2789
8/2789
7/2789
329/2789
152/2789
38/2789
56/2789
34/2789
202/2789