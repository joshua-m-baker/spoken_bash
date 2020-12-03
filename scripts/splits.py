
from sklearn.model_selection import train_test_split
import os

def path(*args):
    return os.path.realpath(os.path.join(os.path.dirname(__file__), *args))


with open(path("..", "data", "src-full.txt")) as f:
    source = f.readlines()

with open(path("..", "data", "tgt-full.txt")) as f:
    target = f.readlines()


X_1, X_test, y_1, y_test = train_test_split(source, target, test_size=0.1, random_state=0)

X_train, X_dev, y_train, y_dev = train_test_split(X_1, y_1, test_size=0.11, random_state=0)

with open(path("..", "data", "src-train.txt"), 'w') as src_train:
    src_train.writelines(X_train)

with open(path("..", "data", "tgt-train.txt"), 'w') as tgt_train:
    tgt_train.writelines(y_train)

with open(path("..", "data", "src-test.txt"), 'w') as src_test:
    src_test.writelines(X_test)

with open(path("..", "data", "tgt-test.txt"), 'w') as tgt_test:
    tgt_test.writelines(y_test)

with open(path("..", "data", "src-dev.txt"), 'w') as src_dev:
    src_dev.writelines(X_dev)

with open(path("..", "data", "tgt-dev.txt"), 'w') as tgt_dev:
    tgt_dev.writelines(y_dev)
