from flask import request, Blueprint

import controllers


quilts = Blueprint('quilts', __name__)


@quilts.route('/quilt', methods=['POST'])
def quilt_add():
    return controllers.quilt_add(request)


@quilts.route('/quilts', methods=['GET'])
def quilts_get_all():
    return controllers.quilts_get_all(request)


@quilts.route('/quilt/<quilt_id>', methods=['GET'])
def quilt_get_by_id(quilt_id):
    return controllers.quilt_get_by_id(request, quilt_id)


@quilts.route('/quilt/<quilt_id>', methods=['DELETE'])
def quilt_delete_by_id(quilt_id):
    return controllers.quilt_delete_by_id(request, quilt_id)


@quilts.route('/quilts/<user_id>', methods=['GET'])
def quilts_get_by_user(user_id):
    return controllers.quilts_get_by_user(request, user_id)


@quilts.route('/quilt/<quilt_id>', methods=['PUT'])
def quilt_update(quilt_id):
    return controllers.quilt_update(request, quilt_id)


@quilts.route('/quilt/activity/<quilt_id>', methods=['PATCH'])
def quilt_activity(quilt_id):
    return controllers.quilt_activity(request, quilt_id)


@quilts.route('/quilt/image-add/<quilt_id>', methods=['POST'])
def quilt_add_image(quilt_id):
    return controllers.quilt_add_image(request, quilt_id)