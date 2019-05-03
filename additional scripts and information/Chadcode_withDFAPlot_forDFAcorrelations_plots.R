
gene.data <- read.csv("/Users/mramsey/Desktop/endogenous for R.csv")

gene.reduced <- gene.data[,65:76]

gene.reduced <- read.csv("/Users/mramsey/Desktop/gene.reduced.csv")

#PCA Analyses
pc <- prcomp(gene.reduced, scale=TRUE)
summary(pc)

#Get PC scores 

pc.scores <- pc$x

#Get PC loadings 

pc.loadings <- pc$rotation

#Get DFA for data

#read in with categories for DFA

gene.dfa <- read.csv("Users/chadbrock/Desktop/Field Work Files/gene.reduced.csv")
gene.dfa <- as.matrix(gene.dfa)
dfa <- lda(gene.dfa[,13] ~ gene.dfa[,2:12])
pred.res <- predict(dfa)
DFAscores <- pred.res$x
dfa.table <- table(gene.dfa[,13], pred.res$class)
diag(prop.table(dfa.table, 1))

# total percent correct
sum(diag(prop.table(dfa.table)))

#ANOVA on DFA axes

summary(aov(DFAscores[,1] ~factor(gene.dfa[,13])))

#DFA Plot

one <- chull(DFAscores[1:5, 1:2])
two <- chull(DFAscores[6:12, 1:2])
three <- chull(DFAscores[13:17, 1:2])
four <- chull(DFAscores[18:23, 1:2])
five <- chull(DFAscores[24:30, 1:2])

one <- c(one, one[1])
two <- c(two, two[1])
three <- c(three, three[1])
four <- c(four, four[1])
five <- c(five, five[1])

plot(DFAscores[,2] ~ DFAscores[,1], col = gene.dfa[,13], pch = gene.dfa[,13], xlab="DF Axis 1", ylab="DF Axis 2" , main = "DFA For Gene Expression Data")

lines(DFAscores[1:5,1:2][one,], col="1")
lines(DFAscores[6:12,1:2][two,], col="2")
lines(DFAscores[13:17,1:2][three,], col="3")
lines(DFAscores[18:23,1:2][four,], col="4")
lines(DFAscores[24:30,1:2][five,], col="5")

leg.txt <- c("One", "Two", "Three", "Four", "Five")

legend("topright", legend = leg.txt, ncol =2, col=1:5, pch=1:5, lty=1, merge=TRUE)

## ANCOVA for resdiduals

ancova <- lm(pc$x[,1]~lake[1:129]*depth[1:129])
summary(ancova)
residuals <- ancova$residuals


#Loop to calculate R between DFA's and Raw Data


DFA_axes2 <- function(DF, Data) {


    DFA.REG.results <- matrix(nrow=length(colnames(DF)), ncol=length(colnames(Data)))
    
	colnames(DFA.REG.results) <- c(1:length(colnames(Data)))
	
	rownames(DFA.REG.results) <- c(1:length(colnames(DF)))

	
 	for (i in 1:length(colnames(DF))) {
 		
 		for (j in 1:length(colnames(Data))) {

			
			s <- cor.test(DF[,i] , Data[,j])
			
			DFA.REG.results[i , j] <- s$estimate
						
			}
		
				
			}
			
			
			return(DFA.REG.results)

}


#Loop to calculate R2 between DFA's and Raw Data

DFA_axes <- function(DF, Data) {


    DFA.REG.results <- matrix(nrow=length(colnames(DF)), ncol=length(colnames(Data)))
    
	colnames(DFA.REG.results) <- c(1:length(colnames(Data)))
	
	rownames(DFA.REG.results) <- c(1:length(colnames(DF)))

	
 	for (i in 1:length(colnames(DF))) {
 		
 		for (j in 1:length(colnames(Data))) {
		
			
			anova(DFA.lm <- lm(DF[,i] ~ Data[,j]))
			s <- summary(DFA.lm <- lm(DF[,i] ~ Data[,j]))
		
			DFA.REG.results[i , j] <- s$r.squared
			
			}
		
			}
			
			return(DFA.REG.results)

}

##Calculate R and r2 for the original data regressed on each DFA axis

r.values <- DFA_axes2(DFAscores, gene.dfa[,2:12])

r2.values <- DFA_axes(DFAscores, gene.dfa[,2:12])


#Makes Plots for DFA/Raw Data Correlation. This is per gene (below is for the first gene)

X_scale <- 1:11

zero.line <- rep(0, length(X_scale))

plot(X_scale, r.values[1,], ylim = c(-1.5, 1.5) , pch="" , xlab="DF Axis #)", ylab="R" , main = "R for DFA vs. Raw Data")

lines(spline(X_scale, r.values[1,]), col="1")

lines(spline(X_scale, zero.line), lty=2)


