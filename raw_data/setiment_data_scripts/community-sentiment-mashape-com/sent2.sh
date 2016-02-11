# Taken from https://github.com/Charudatt89/Personality_Recognition/blob/master/22-9-PersonalityRecognition/SourceCode/FEATURE_BASED_APPROACH/ source_code/run_sentiment_8.sh
cd /home/jm/Documents/caseSolvingSeminar/raw_data
file=data_statuses_only.csv
while IFS= read -r line
do
	echo $line         
	# echo line is stored in $line
	tmp=`curl -d "txt=$line" https://community-sentiment.p.mashape.com/text/ -H "X-Mashape-Key: Gkqp1Q0amCmsh2nUi5qabMR97LY2p1eXbQjjsnEEvzsCQmyU15" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json" `
	echo $tmp >> /home/jm/Documents/caseSolvingSeminar/raw_data/setiment_data_scripts/community-sentiment-mashape-com/result2.json
	echo "-----------------"
done < "$file"
echo "-----------------------"
#echo $tmp
echo "--------"
