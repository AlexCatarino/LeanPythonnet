using System;
using Python.Runtime;
using ImpromptuInterface;

namespace LeanPythonnet
{
    class Program
    {
        static void Main(string[] args)
        {
            IAlgorithm algorithmInstance;

            try
            {
                PythonEngine.Initialize();

                using (Py.GIL())
                {
                    dynamic scope = Py.Import("BasicTemplateAlgorithm");

                    dynamic item = scope.BasicTemplateAlgorithm();

                    algorithmInstance = Impromptu.ActLike<IAlgorithm>(item);
                }
                
                algorithmInstance.Initialize();
                algorithmInstance.SetCash(1000000);
                
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            Console.Write("Done.");
            Console.ReadKey();
        }
    }
}