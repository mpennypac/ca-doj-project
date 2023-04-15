

data = read.csv('All Annual Data.csv')
data = data[,c(1, 2, 3, 4, 5, 6, 8, 13, 27, 33, 47, 51, 67)]

## so data is all set up, we just need the intervention series which
## should be pretty easy to construct.

## the first intervention series is what we care about the most (and expect
## to have the largest effect): the January 2018 change in the penal code.
## Unfortunately we lost the ability to be as specific as which month we're looking at
## with the some of the data, so we'll have to settle for the intervention occurring
## just in the year 2018, which is index #30.

intervention1 = c(rep(0, 30), rep(1, (33-30)))
data$`2018 Policy` = intervention1
## we'll just assume the effect is immediate for now, maybe we'll compare to a
## slightly different series where it takes 1 year to affect anything (which
## is literally just making the first 1 a 1/2 instead)

## next is the court ruling in 2003 that made it so people can only
## get their arrest records sealed with "factual innocence," not just
## acquittal. Same thing now but with the intervention occurring in 2003,
## or at index #15.

intervention2 = c(rep(0, 15), rep(1, (33-15)))
data$`2003 Decision` = intervention2

## now is the 2009 decision that I expect to have the weakest effect (if anything)
## where the kind of person who can successfully seal their criminal record
## was made clear to be... well not the guy who petitioned for it at least.
## 2009 is index #21.

intervention3 = c(rep(0, 21), rep(1, (33-21)))
data$`2009 Decision` = intervention3


## now we just do a VaR analysis, looking at how each intervention affected the biggest
## variables of interest (i.e. the economic indicators as well as the total number of
## violent crimes, homicides, and robberies -- it's made pretty clear that this isn't necessarily
## intended to change how many sex-related crimes there are in the 2023 legislation.)

library(vars)
model = VAR(data[,-c(1, 14, 15, 16)],p=1,exogen=data[,c(14, 15, 16)])
print(summary(model))

years = ts(c(1989:(1989+nrow(data)-1)))
par(cex.lab=0.75,cex.axis=1)
plot_data1 = ts(data[,c(2, 3, 4)],start=1989)
plot.ts(plot_data1,main='Basic Economic Indicators',xlab='Years')
abline(v=2003,col='black',lty=2)
abline(v=2009,col='black',lty=2)
abline(v=2018,col='black',lty=2)
plot_data2 = ts(data[,c(5, 6)],start=1989)
plot.ts(plot_data2,main='Basic Economic Indicators',xlab='Years')
abline(v=2003,col='black',lty=2)
abline(v=2009,col='black',lty=2)
abline(v=2018,col='black',lty=2)
#addLegend('bottomleft',legend=c('2003 Decision','2009 Decision','2018 Policy Change'),
#       col=c('coral','blue4','green3'),lty=2,bty='n')


years = c(1989:(1989+nrow(data)-1))
par(cex.lab=0.75,cex.axis=1)
plot(years,data$Violent.Crimes,type='l',col='black',main='Crime Statistics',xlab='Year',ylab='Number of Crimes Committed',ylim=c(2000,1750000))
lines(years,data$Robbery,col='red')
lines(years,data$Aggravated.Assault,col='blue')
lines(years,data$Property.Crimes,col='brown')
lines(years,data$Motor.Vehicle.Theft,col='purple')
lines(years,data$Larceny.Theft,col='orange')
lines(years,data$Arson,col='darkgray')
abline(v=2003,col='black',lty=2)
abline(v=2009,col='black',lty=2)
abline(v=2018,col='black',lty=2)
legend(25+1989-1, 1775000, legend=c('Violent Crimes', 'Robbery', 'Aggravated Assault', 'Property Crimes', 'Motor Vehicle Theft','Larceny Theft','Arson'),
       col=c('black','red','blue','brown','purple','orange','darkgray'),lty=1:1)
#legend(24.75+1985-1,1319000,legend=c('2003 Decision','2009 Decision','2018 Policy Change'),
#       col=c('coral','blue4','green3'),lty=2,bty='n')














