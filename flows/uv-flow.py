from metaflow import FlowSpec, step


class UVFlow(FlowSpec):
    """
    A flow to test the metaflow uv integration
    """

    @step
    def start(self):
        import pandas as pd

        print(pd.__version__)
        self.next(self.end)

    @step
    def end(self):
        """Now import the custom package and do stuff with it."""
        from metaflow_uv import hello_world

        hello_world()


if __name__ == "__main__":
    UVFlow()