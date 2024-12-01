# Particle Accelerator MIddle LAyer (PAMILA) - Python middle layer package for control of particle accelerators, compatible with bluesky / ophyd / tiled

## Environment setup

`$ conda create -n pamila python=3.11 poetry numpy=1 scipy pint pyepics caproto h5py matplotlib=3.8 ipython jupyter ipympl tables black pre-commit pydantic=2.9 -c conda-forge`

(Note that pydantic=2.10 causes an error when the `ge` arg of `Field()` is a
non-jsonable object like `pint.Quantity()` as of 11/27/2024. v2.9 works.)

Then activate the created environment:

`$ conda activate pamila`

Now you need to specify some environment variables for this environment. Run
the following two commands:

```
(pamila) $ echo 'export PAMILA_FACILITY="nsls2"' > $(dirname $(dirname $(which python)))/etc/conda/activate.d/pamila_activate.sh

(pamila) $ echo 'unset PAMILA_FACILITY' > $(dirname $(dirname $(which python)))/etc/conda/deactivate.d/pamila_deactivate.sh
```

"nsls2" in `pamila_activate.sh` should be replaced with your facility name.

Deactivate and re-activate the environment for this environment variable setup
to take effect, and confirm it:

```
(pamila) $ conda deactivate
$ conda activate pamila
(pamila) $ echo $PAMILA_FACILITY
nsls2
```

Install other dependent packages with `pip`:

```
(pamila) $ pip install ophyd
(pamila) $ pip install bluesky==1.13
(pamila) $ pip install tiled[all]
(pamila) $ pip install accelerator-toolbox
```
# How to install `pamila` with `poetry`

```
(pamila) $ git clone https://github.com/python-accelerator-middle-layer/pamila.git
(pamila) $ cd pamila
(pamila) $ poetry build
(pamila) $ pip install dist/pamila-0.1.0-py3-none-any.whl
```

If the actual wheel file name generated by the `poetry build` command is
different from `pamila-0.1.0-py3-none-any.whl`, use the actual file name.

If you modify the source for `pamila` and re-install it, you can run the following
commands instead:

```
(pamila) $ poetry build
(pamila) $ pip install dist/pamila-0.1.0-py3-none-any.whl --force-reinstall --no-deps
```

# `pre-commit` setup

Before `pre-commit` starts automatically formats all the files included in the
git repository, it needs to be set up as follows:

```
(pamila) $ cd pamila
(pamila) $ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```