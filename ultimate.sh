cd Letters_stash_for_sounds/


sleep 2

while true ; do 

yo=$(ls -Art | tail -n1)




if [ "$yo" == "A.txt" ]; then 
echo The Letter is A  
play A.mp3
sleep 2


elif [ "$yo" == "B.txt" ]; then 
echo The Letter is B 
play B.mp3
sleep 2



elif [ "$yo" == "D.txt" ]; then 
echo The Letter is D
play D.mp3
sleep 2


elif [ "$yo" == "F.txt" ]; then 
echo The Letter is F 
play F.mp3
sleep 2


elif [ "$yo" == "H.txt" ]; then 
echo The Letter is H 
play H.mp3
sleep 2


elif [ "$yo" == "I.txt" ]; then 
echo The Letter is I 
play I.mp3
sleep 2


elif [ "$yo" == "B.txt" ]; then 
echo The Letter is B 
play B.mp3
sleep 2


elif [ "$yo" == "L.txt" ]; then 
echo The Letter is L
play L.mp3
sleep 2



elif [ "$yo" == "U.txt" ]; then 
echo The Letter is U
play U.mp3
sleep 2



elif [ "$yo" == "V.txt" ]; then 
echo The Letter is V 
play V.mp3
sleep 2


elif [ "$yo" == "W.txt" ]; then 
echo The Letter is W 
play W.mp3
sleep 2



elif [ "$yo" == "Y.txt" ]; then 
echo The Letter is Y
play Y.mp3
sleep 2


elif [ "$yo" == "CALIBRATE.txt" ]; then 
echo Its Calibrated  
play CALIBRATE.mp3
sleep 2


elif [ "$yo" == "C.txt" ]; then 
echo The Letter is C
play C.mp3
sleep 2



elif [ "$yo" == "J.txt" ]; then 
echo The Letter is J 
play J.mp3
sleep 2


fi


done






