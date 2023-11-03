# Data source
# https://www.arpalazio.net/main/aria/sci/basedati/chimici/chimici.php

# Set parameters
ada <- 39 # ID monitoring station
years <- 2015:2022  #Years to download
poll <- c("PM10", "PM2.5", "SO2", "NO2", "O3", "CO", "NO", "NOX") #Observed parameters

# create an empty data.frame with dates
start_date <- as.Date(paste0(years[1],"-01-01"))
end_date <- as.Date(paste0(years[length(years)],"-12-31"))
date_seq <- seq.Date(start_date, end_date, by="day")
pollutant <- data.frame(date_p=date_seq)

# For each pollutant, for each year, download file, read file, 
# look for data for my monitoring station, append data
for (p in poll){
  # initialize parameters to extract from file
  year <- c()
  day <- c()
  val <- c()
  for (a in years){
    print(paste(p, a))
    # download file
    url <- paste0("https://www.arpalazio.net/main/aria/sci/basedati/chimici/BDchimici/RM/MedieGiornaliere/RM_",p, "_", a, "_gg.txt")
    download.file(url, destfile="temp.txt")
    # read file
    x <- read.table("temp.txt", header=T, na.strings = "-999.0")
    year <- c(year, x[,1])
    day <- c(day, x[,2])
    # find monitoring station
    id <- which(names(x)==paste0("X", ada))
    if (length(id) == 1){
      val <- c(val, x[,id])
    } else{
      val <- c(val, rep(NA, nrow(x)))
    }
  }
  # recognize dates
  date_p <- as.Date(paste(year, day), "%Y %j")
  # create data.frame for single pollutant
  poll1 <- data.frame(date_p, val)
  names(poll1)[2] <- p
  #merge into the final data.frae
  pollutant <- merge(pollutant, poll1, by="date_p", all.x=T)
}

# write final data.frame on a file
write.table(pollutant, file="Pollution_Villa_Ada.csv", col.names = T, row.names = F, quote=F, sep=";")

#Plot results
plot(pollutant$date_p, pollutant$PM10, type="l", main="Pollution", xlab="dates", ylab="PM Concentration")
lines(pollutant$date_p, pollutant$PM2.5, col=2)
abline(h=50, col="green")
legend("top", legend=c("PM_10", "PM_2.5"),col=1:2, lty=1, horiz = T)
