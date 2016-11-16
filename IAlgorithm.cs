namespace LeanPythonnet
{
    public interface IAlgorithm
    {
        void Initialize();
        void OnData(int data);
        void SetStartDate(int year, int month, int day);
        void SetEndDate(int year, int month, int day);
        void SetCash(double cash);
    }
}