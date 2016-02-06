# main.R
library(ggmap)

conn <- dbConnect(MySQL(), dbname = "hackthon", username="root", password="XuWenzhaO", host="127.0.0.1", port=3306)

charlotte_sql <- "Select latitude, longitude from businessSub where city='Charlotte'"
madison_sql <- "Select latitude, longitude from businessSub where city='Madison'"
tempe_sql <- "Select latitude, longitude from businessSub where city='Tempe'"
henderson_sql <- "select latitude,longitude from businessSub where city='Henderson'"
LasVegas_sql <- "select latitude,longitude from businessSub where city='Las Vegas'"

# Charlotte
# Madison
# Tempe
# Henderson
# Las Vegas

plotBusinessLocation <- function(conn,sql,city){
	position <- dbGetQuery(conn,sql)
	p <- qmplot(longitude,latitude,data=position)+ggtitle(city)
	png(paste("./figures/",city,".png"))
	print(p)
	dev.off()
}


plotBusinessLocation(conn,charlotte_sql,"Charlotte")
plotBusinessLocation(conn,madison_sql,"Madison")
plotBusinessLocation(conn,tempe_sql,"Tempe")
plotBusinessLocation(conn,henderson_sql,"Henderson")
plotBusinessLocation(conn,LasVegas_sql,"Las Vegas")




# aHc3R3YV2sMY57RyGXw5qw   



# check the average stars in spatial location

sql <- "select * from (select AVG(stars),business_id from reviews group by business_id) as subreviews right join (select business_id, longitude,latitude,city from businessSub) as businessLocation on subreviews.business_id = businessLocation.business_id"
business_rate <- dbGetQuery(conn,sql)

for(cityName in c("Charlotte","Madison","Tempe","Henderson","Las Vegas")){
	p <- qmplot(longitude,latitude,data=subset(business_rate,city==cityName),color=avg_star)+scale_colour_gradient(low="red",high="green")
	png(paste("./figures/avg_rate_",cityName,sep=""))
	print(p)
	dev.off()
}


# ikm0UCahtK34LbLCEw4YTw has been the most cities

by_city_summarise <- group_by(by_city,user_id)

