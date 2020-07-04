from classes import Queue


def hot_potato(names,eliminate):
    kids = Queue()

    # initialise the queue:
    for kid_name in names:
        kids.enqueue(kid_name)

    print("Starting queue: {}".format(names))
    while kids.size() > 1:
        for i in range(eliminate):
            kids.enqueue(kids.dequeue())

        kid_to_eliminate = kids.dequeue()
        print("Eliminated {}".format(kid_to_eliminate))

    print("{} survived!".format(kids.dequeue()))


