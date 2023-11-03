install.packages("httr")
library(httr)

# Explore the API service
# https://open-meteo.com/


######################################
# Weather forecast in Luiss (latitude 41.92 N, longitude 12.49 E)
api_url <- "https://api.open-meteo.com/v1/forecast?latitude=41.92&longitude=12.49&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

sample <- GET(api_url)

### Or (composing the query starting from the root)
lat <- 41.92
lon <- 12.49
curr <- "true"
hou <- "temperature_2m,relativehumidity_2m,windspeed_10m"

sample <- GET("https://api.open-meteo.com/v1/forecast", 
               query = list(latitude = lat, 
                            longitude = lon,
                            current_weather = curr,
                            hourly=hou))
### Explore the data
x <-  content(sample)

# parameters
date_str <- unlist(x$hourly$time)
temp <- unlist(x$hourly$temperature_2m)
rh <- unlist(x$hourly$relativehumidity_2m)

# dates and times
date_dtt <- strptime(date_str, "%Y-%m-%dT%H:%M", tz="GMT")

# build the dataframe
my_dataset <- data.frame(datetime=date_dtt, temperature = temp, rh= rh)
str(my_dataset)

#plot
plot(my_dataset$datetime, my_dataset$temperature, type="l")




# Historical data Luiss (latitude 41.92 N, longitude 12.49 E)
#"https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"

lat <- 41.92
lon <- 12.49
start <- "2022-10-01"
end <- "2023-09-30"
hou <- "temperature_2m"

sample2 <- GET("https://archive-api.open-meteo.com/v1/era5", 
               query = list(latitude = lat, 
                            longitude = lon,
                            start_date = start,
                            end_date= end,
                            hourly=hou))

result2 <- content(sample2)
dates <- unlist(result2$hourly$time)
dates_corr <- strptime(dates, "%Y-%m-%dT%H:%M", tz="GMT")
temp <- unlist(result2$hourly$temperature_2m)

plot(temp, type="l")

plot(dates_corr, temp, type="l")

# suppose to  delete some items
idcanc <- 6000:7500

temp2 <- temp[-idcanc]
date2 <- dates_corr[-idcanc]

par(mfrow=c(1,2))
plot(temp2, type="l")
plot(date2, temp2, type="l")

