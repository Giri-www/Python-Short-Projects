@echo off
echo %date% %time% > "C:\Users\Rahul\Desktop\New folder (8)\New folder\script_output.log"
call "C:\Users\Rahul\Desktop\New folder (8)\New folder\scripvenv\Scripts\activate.bat" >> "C:\Users\Rahul\Desktop\New folder (8)\New folder\script_output.log" 2>&1
where python >> "C:\Users\Rahul\Desktop\New folder (8)\New folder\script_output.log" 2>&1
python --version >> "C:\Users\Rahul\Desktop\New folder (8)\New folder\script_output.log" 2>&1
python "C:\Users\Rahul\Desktop\New folder (8)\New folder\insertscripts.py" >> "C:\Users\Rahul\Desktop\New folder (8)\New folder\script_output.log" 2>&1
