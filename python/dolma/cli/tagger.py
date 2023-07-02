from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from typing import List, Optional

from omegaconf import DictConfig
from omegaconf import OmegaConf as om

from dolma.cli import BaseCli
from dolma.core.runtime import TaggerProcessor


class TaggerCli(BaseCli):
    @classmethod
    def make_parser(cls, parser: ArgumentParser):
        parser.add_argument(
            "-c",
            "--config",
            required=True,
            type=str,
            help="Path to the config file",
        )

    @classmethod
    def run_from_args(cls, args: Namespace, existing_config: Optional[dict] = None):
        raise NotImplementedError("TODO: Implement this")
        # config = om.load(args.config)
        # assert isinstance(config, DictConfig)

        # config_dict = om.to_container(config)
        # assert isinstance(config_dict, dict)
        # mixer(config_dict)
