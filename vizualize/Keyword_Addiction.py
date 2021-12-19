#Этот метод отлично подходит для визуализации слово - количевсто (частота встречи слова в списке слов)
def barplot(x_data, y_data, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    #Отрисовка полос, которые будут располагатся в центре деления на оси x.
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    plt.xticks(rotation=90)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    
#Вывод графиков  вцикле
for i in range(0, len(fdf.columns)-1, 2):
    barplot(fdf[fdf.columns[i]], fdf[fdf.columns[i+1]], "Ключевые слова", "Количество слов", "Зависимость категории обращения\nот ключевых слов для категории")
