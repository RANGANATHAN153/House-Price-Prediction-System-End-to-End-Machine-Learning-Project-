{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b3a895d1-a69b-47fa-bd48-6f6122877cea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
      " * Running on http://127.0.0.1:5000\n",
      "\u001b[33mPress CTRL+C to quit\u001b[0m\n",
      " * Restarting with watchdog (inotify)\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/runpy.py\", line 198, in _run_module_as_main\n",
      "    return _run_code(code, main_globals, None,\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/runpy.py\", line 88, in _run_code\n",
      "    exec(code, run_globals)\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/ipykernel_launcher.py\", line 18, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/traitlets/config/application.py\", line 1074, in launch_instance\n",
      "    app.initialize(argv)\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/traitlets/config/application.py\", line 118, in inner\n",
      "    return method(app, *args, **kwargs)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/ipykernel/kernelapp.py\", line 692, in initialize\n",
      "    self.init_sockets()\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/ipykernel/kernelapp.py\", line 331, in init_sockets\n",
      "    self.shell_port = self._bind_socket(self.shell_socket, self.shell_port)\n",
      "                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/ipykernel/kernelapp.py\", line 253, in _bind_socket\n",
      "    return self._try_bind_socket(s, port)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/ipykernel/kernelapp.py\", line 229, in _try_bind_socket\n",
      "    s.bind(\"tcp://%s:%i\" % (self.ip, port))\n",
      "  File \"/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/zmq/sugar/socket.py\", line 320, in bind\n",
      "    super().bind(addr)\n",
      "  File \"zmq/backend/cython/_zmq.py\", line 1009, in zmq.backend.cython._zmq.Socket.bind\n",
      "  File \"zmq/backend/cython/_zmq.py\", line 190, in zmq.backend.cython._zmq._check_rc\n",
      "zmq.error.ZMQError: Address already in use (addr='tcp://127.0.0.1:42165')\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3707: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "model = joblib.load(\"house_price_model.pkl\")\n",
    "loc_enc = joblib.load(\"location_encoder.pkl\")\n",
    "prop_enc = joblib.load(\"property_encoder.pkl\")\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "\n",
    "    area = float(request.form['area'])\n",
    "    bedrooms = int(request.form['bedrooms'])\n",
    "    bathrooms = int(request.form['bathrooms'])\n",
    "    age = int(request.form['age'])\n",
    "\n",
    "    location = loc_enc.transform([request.form['location']])[0]\n",
    "    property_type = prop_enc.transform([request.form['property_type']])[0]\n",
    "\n",
    "    data = np.array([[area, bedrooms, bathrooms, age, location, property_type]])\n",
    "\n",
    "    prediction = model.predict(data)\n",
    "\n",
    "    return render_template('index.html', prediction_text=f\"Predicted Price: ₹{int(prediction[0])}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2025.12-py312",
   "language": "python",
   "name": "conda-env-anaconda-2025.12-py312-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
