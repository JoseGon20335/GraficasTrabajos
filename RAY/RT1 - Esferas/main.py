import ray

# falta arreglar


def main():
    r = ray.RayT(800, 800)
    r.dense = 1
    r.point(100, 100)
    r.render()

    r.write()


main()
