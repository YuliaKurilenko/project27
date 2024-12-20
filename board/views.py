def add_likes(request, pk):
    """
    Добавление лайков
    """
    like = Advertisement.objects.get(pk=pk)
    if request.method == "GET":
        like.likes += 1
        like.save()
        return redirect('board:advertisement_detail', pk=pk)
    return render(request, 'board/advertisement_detail.html')


def add_dislikes(request, pk):
    """
    Добавление дизлайков
    """

    like = Advertisement.objects.get(pk=pk)
    if request.method == "GET":
        like.dislikes += 1
        like.save()
        return redirect('board:advertisement_detail', pk=pk)
    return render(request, 'board/advertisement_detail.html')
