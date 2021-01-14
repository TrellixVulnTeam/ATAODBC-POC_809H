import re
import json
from pprint import pprint
import os
import platform


def initPlanSettings(settings):
    repo = os.environ.get('GITHUB_REPOSITORY')
    workflow = os.environ.get('GITHUB_WORKFLOW')
    ref = os.environ.get('GITHUB_REF')
    job = os.environ.get('GITHUB_JOB')
    category, product, type = (repo.split('/')[-1]).split('-')
    plan_type, env = workflow.split('-')
    branch = ref.split('/')[-1]
    category = category.strip()
    product = product.strip()
    type = type.strip()
    plan_type = plan_type.strip()
    env = env.strip()
    print env
    distribution, compiler, bitness = env.split().strip()
    branch = branch.strip()

    settings['platform'] = ''
    settings['project'] = category + type
    settings['product'] = product
    settings['product_lower'] = product.lower()
    settings['branch'] = branch
    settings['plantype'] = ''
    settings['distribution'] = distribution
    settings['compiler'] = compiler
    settings['plan'] = ''
    settings['job'] = job
    settings['buildtarget'] = ''
    settings['bitness'] = bitness
    settings['drivertype'] = ''
    settings['dm_name'] = ''
    settings['dm_version'] = ''
    settings['dm'] = ''
    settings['jre'] = ''
    settings['test_platform'] = ''
    settings['package_platform'] = ''
    settings['os_arch'] = ''
    settings['testtype'] = ''
    settings['packagetype'] = ''
    settings['packageformat'] = ''

    return settings


def initCompilerSettings(planSettings):
    settings = {}
    return settings