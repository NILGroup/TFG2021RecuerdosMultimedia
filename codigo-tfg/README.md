# Un sistema de diálogo generativo para la terapia de la reminiscencia
Nuestro trabajo consiste en el desarrollo de un sistema que sea capaz deextraer descripciones de elementos presentes en material multimedia, comofotografías, que puedan representar recuerdos para personas con problemasde memoria.
El sistema extraerá elementos de las imágenes y generará preguntas rela-cioandas con esta. Además, el sistema será capaz de responder a la personaen función de sus respuestas y continuará haciendo preguntas para contuniarla conversacion.
De esta forma, las personas con problemas de memoria tendrán una he-rramienta útil para poder ejercitarla y recordar cosas sobre su vida y supasado.Para el desarrollo de este sistema se utilizarán distintas técnicas de Deeplearning, como por ejemplo redes convolucionales y recurrentes.

## Pasos para ejecutar la terapia de reminiscencia automática en Telegram con los modelos entrenados:

1. Instale las bibliotecas necesarias mediante src / requirements.txt -> 'pip install -r requirements.txt'
2. Cree un nuevo bot, las instrucciones se pueden encontrar aquí: https://core.telegram.org/bots, solo tiene que hablar con BotFather para obtener el token que se requiere para autorizar el bot y enviar solicitudes a la API del bot.
     El token es una cadena del tipo 110201543: AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw.
3. Una vez creado el bot, coloque el token en telegram_bot.py y podrá pasarlo por argumento.
4. Descargue los puntos de control del modelo de https://1drv.ms/u/s!Ah93nVed1CWhgRcuqbIFDMKWFDlX?e=KXMZoL y coloque las carpetas en el directorio / src
5. Ejecute telegram_bot.py -> python telegram_bot.py --token 110201543: AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
6. Para iniciar la Terapia de Reminiscencia, busque el bot que creó en Telegram y escriba el comando /start
    

