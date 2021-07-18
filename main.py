from selenium import webdriver
import math
import time
import os
import eel

eel.init('web')


def getUrl(url, volume, chapter):
    if url[-1] != '/':
        url += '/'
    return str(url) + 'v' + str(volume) + '/c' + str(chapter)


def startDriver(url, chapterNumbers, outputFolder='', outputName='output', firstChapter=1, volumeNumber=1):
    options = webdriver.FirefoxOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--headless')
    chapter = firstChapter
    url = getUrl(url, volumeNumber, chapter)
    print('Запуск парсинга...')
    eel.consoleArea('Запуск парсинга...')
    for i in range(firstChapter, chapterNumbers + 1):
        try:
            print(i)
            eel.consoleArea(i)
            driver = webdriver.Firefox(
                executable_path='geckodriver.exe',
                options=options
            )
            driver.get(url=url)
            outputSource = 'output/' + outputFolder + '/' + outputName + '_c' + str(chapter) + '.txt'
            title = 'Том '+str(volumeNumber)+' глава '+str(chapter)+'\n'
            time.sleep(5)
            print('Запись файла...')
            eel.consoleArea('Запись файла...')
            p = driver.find_element_by_xpath("//*[@class='reader-container container container_center']")
            t = title + p.text
            with open(outputSource, 'w', encoding='utf-8') as file:
                file.write(t)
            print('[' + str(chapter) + '] глава готова')
            eel.consoleArea('[' + str(chapter) + '] глава готова')
            url = driver.find_element_by_xpath(
                "//*[@class='reader-next__btn button text-truncate button_label button_label_right']").get_attribute(
                "href")
            chapter += 1
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


# url = 'https://ranobelib.me/sss-class-suicide-hunter'
# chapterNumbers = 1
# outputFolder = 'F:/Project/Python/RanobeLib downloader/output/SSS-Class Suicide Hunter'
# outputName = 'SSS-Class Suicide Hunter'
# firstChapter = 1
# volumeNumber = 1

@eel.expose
def start(url, chapterNumbers, outputFolder, outputName, firstChapter, volumeNumber):

    url = str(url)
    chapterNumbers = int(chapterNumbers)
    outputFolder = str(outputFolder)
    outputName = str(outputName)
    firstChapter = int(firstChapter)
    volumeNumber = int(volumeNumber)

    t0 = time.time()

    if not os.path.exists('output/' + outputFolder):
        os.mkdir('output/' + outputFolder)
    outFile = open('output/' + outputFolder + '/outFile.txt', 'w', encoding='utf-8')
    startDriver(url, chapterNumbers, outputFolder, outputName, firstChapter, volumeNumber)

    t1 = time.time() - t0
    print("Time elapsed: ", math.ceil(t1), "second")
    eel.consoleArea("Прошло: " + str(math.ceil(t1)) + " секунд" + '\n' + "Глав сохранено: " + str(chapterNumbers))
    outFile.write(
        "Прошло: " + str(math.ceil(t1)) + " секунд" + '\n' + "Глав сохранено: " + str(chapterNumbers)
    )

eel.start('index.html', size=(700, 700))