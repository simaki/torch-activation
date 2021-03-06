import pathlib

import matplotlib.pyplot as plt
import mpl_hig
import torch


def get_activations():
    yield torch.nn.ELU()
    yield torch.nn.Hardshrink()
    yield torch.nn.Hardsigmoid()
    yield torch.nn.Hardtanh()
    yield torch.nn.Hardswish()
    yield torch.nn.LeakyReLU()
    yield torch.nn.LogSigmoid()
    # yield torch.nn.MultiheadAttention()
    # yield torch.nn.PReLU()
    yield torch.nn.ReLU()
    yield torch.nn.ReLU6()
    yield torch.nn.RReLU()
    yield torch.nn.SELU()
    yield torch.nn.CELU()
    yield torch.nn.GELU()
    yield torch.nn.Sigmoid()
    yield torch.nn.SiLU()
    yield torch.nn.Softplus()
    yield torch.nn.Softshrink()
    yield torch.nn.Softsign()
    yield torch.nn.Tanh()
    yield torch.nn.Tanhshrink()
    yield torch.nn.Threshold(threshold=1, value=1)


def draw(activation):
    torchcolor = "#EE4C2C"
    name = activation.__class__.__name__
    x = torch.linspace(-6.5, 6.5, 1000)
    y = activation(x)

    plt.figure()
    plt.plot(x, y, color=torchcolor)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.xlim(-6.5, 6.5)
    plt.ylim(-6.5, 6.5)
    plt.title("{} activation function".format(name))
    plt.savefig("fig/{}.png".format(name))
    plt.close()


def write(activation, f):
    name = activation.__class__.__name__
    doc = "https://pytorch.org/docs/stable/generated/torch.nn.{}.html".format(name)
    f.write("## [{} activation function]({})\n\n".format(name, doc))
    f.write("![{} activation function](fig/{}.png)\n\n".format(name, name))


if __name__ == "__main__":
    mpl_hig.set("whitegrid")
    with open("README.md", "w") as f:
        f.write("# PyTorch Activations\n\n")
        for activation in get_activations():
            draw(activation)
            write(activation, f)
